import os
import sys
from pathlib import Path
import frontmatter
from typing import List, Dict

POSTS_DIR = '_posts'
STDIN = sys.stdin.read()

def get_categories(path: Path) -> List[str]:
  post = frontmatter.load(path)
  categories = post.metadata.get('categories', [])
  if type(categories) == str:
    categories = categories.split()
  category: str = post.metadata.get('category')
  if category:
    categories.append(category)
  return categories

def get_category_map(root) -> Dict[str, List[Path]]:
  category_map: Dict[str, List[Path]] = {}
  for file in (root / POSTS_DIR).iterdir():
    categories = get_categories(file)
    if len(categories) != 1:
      raise RuntimeError(f'number of categories does not equal 1 in {file.absolute()}')
    category = categories[0]
    if category not in category_map:
      category_map[category] = [file]
    else:
      category_map[category].append(file)
  return category_map

if __name__ == '__main__':
  root = Path(sys.argv[1])
  if not root.exists():
    raise RuntimeError(f'{root.absolute()} does not exist')
  elif not root.is_dir():
    raise RuntimeError(f'{root.absolute()} is not a directory')
  
  category_map: Dict[str, List[Path]] = get_category_map(root)
  
  for category, files in category_map.items():
    category_dir = root / category
    posts_dir = category_dir / POSTS_DIR

    os.mkdir(category_dir)
    os.mkdir(posts_dir)

    (category_dir / 'index.html').write_text(STDIN.replace('{}', category))
    
    for file in files:
      (posts_dir / file.name).write_text(file.read_text())
