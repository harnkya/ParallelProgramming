def calculate_pyramid_height(blocks):
    height = 0
    total_blocks = 0

    while total_blocks + (height + 1) <= blocks:
        height += 1
        total_blocks += height

    return height
