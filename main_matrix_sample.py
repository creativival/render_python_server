from time import sleep

from build_box import BuildBox


def draw_three_branches(count, branch_length):
    count -= 1
    if count < 0:
        return

    # draw branches
    shorted_branch_length = branch_length * length_ratio
    print('push_matrix')
    build_box.push_matrix()

    # first branch
    build_box.translate(0, branch_length, 0, pitch=angle_to_open, yaw=0, roll=0)
    build_box.draw_line(0, 0, 0, 0, shorted_branch_length, 0, r=1, g=0, b=1)
    draw_three_branches(count, shorted_branch_length)

    # second branch
    build_box.translate(0, branch_length, 0, pitch=angle_to_open, yaw=120, roll=0)
    build_box.draw_line(0, 0, 0, 0, shorted_branch_length, 0, r=1, g=0, b=0)
    draw_three_branches(count, shorted_branch_length)

    # third branch
    build_box.translate(0, branch_length, 0, pitch=angle_to_open, yaw=240, roll=0)
    build_box.draw_line(0, 0, 0, 0, shorted_branch_length, 0, r=1, g=1, b=0)
    draw_three_branches(count, shorted_branch_length)

    print('pop_matrix')
    build_box.pop_matrix()


room_name = "1000"
build_box = BuildBox(room_name)
initial_length = 10
repeat_count = 5
angle_to_open = 30
length_ratio = 0.8

build_box.change_shape('sphere')
build_box.set_command('float')
build_box.draw_line(0, 0, 0, 0, initial_length, 0, r=0, g=1, b=1)

draw_three_branches(repeat_count, initial_length)
build_box.send_data()
