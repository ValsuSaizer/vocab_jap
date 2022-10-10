def returnabs( alist ):
        return abs( alist )

numbers = [1, 8, 9, -6, 9519, -35, 4894, 65, -12.3546, 48.266, -258.323]
print( numbers )
numbers.sort( key=returnabs )
print( numbers )
