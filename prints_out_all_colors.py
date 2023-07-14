def color_list_1(colors1):
       def color_list_2(colors2):
           for n in colors1:
               for x in colors2:
                   if n != x:
                       print(n)
color_list_1(["white", "black", "red"])
color_list_2(["red", "green"])