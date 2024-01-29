def solution(wallpaper):
    is_first = True
    for y, wall in enumerate(wallpaper):
        for x, st in enumerate(wall):
            if st == '#':
                if is_first:
                    min_x, max_x = x, x 
                    min_y, max_y = y, y
                    is_first = False
                else :
                    if x < min_x :
                        min_x = x
                    if x > max_x :
                        max_x = x
                    if y < min_y :
                        min_y = y
                    if y > max_y :
                        max_y = y
                        
    return [min_y, min_x, max_y + 1, max_x + 1]
