def solution(wallpaper):
    answer = []
    x_count = 0
    x_lst = []
    y_lst = []
    for icon in wallpaper:
        if "#" in icon:
            x_lst.append(x_count)
            y_lst += [i for i, char in enumerate(icon) if char == '#']
        x_count += 1    
    answer = [min(x_lst),min(y_lst),max(x_lst)+1,max(y_lst)+1]
    return answer