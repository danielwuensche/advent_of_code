from pathlib import Path
from shapely.ops import unary_union, clip_by_rect
from shapely.geometry import Polygon

path = Path(__file__).parent / Path("input.txt")
upoly = Polygon()

for shape in path.read_text().strip().splitlines():
    sx, sy, bx, by = [
        int(b.split(",")[0].split(":")[0]) for b in shape.split("=")[1:]
    ]
    md = abs(sx - bx) + abs(sy - by)
    upoly = unary_union([upoly, Polygon(
        [(sx, sy + md), (sx - md, sy), (sx, sy - md), (sx + md, sy)]
    )])

interior = clip_by_rect(upoly, 0, 0, 4_000_000, 4_000_000).interiors[0]
x, y = tuple(map(round, interior.centroid.coords[:][0]))
print(x*4_000_000+y)