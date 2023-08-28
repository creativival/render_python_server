from time import sleep
from random import uniform
from build_box import BuildBox


def get_color(color1, co1or2, ratio):
    return (
        color1[0] * ratio + co1or2[0] * (1 - ratio),
        color1[1] * ratio + co1or2[1] * (1 - ratio),
        color1[2] * ratio + co1or2[2] * (1 - ratio))


def draw_three_branches(count, branch_length):
    count -= 1
    if count < 0:
        return

    # draw branches
    ratio = count / repeat_count
    color = get_color(trunk_color, leaf_color, ratio)
    shorted_branch_length = branch_length * length_ratio
    print('push_matrix')
    build_box.push_matrix()

    # first branch
    build_box.clear_data()
    build_box.change_shape('sphere')
    build_box.set_command('float')
    first_branch_length = branch_length * length_ratio * uniform(0.8, 1.2)
    first_branch_angle = angle_to_open * uniform(0.8, 1.2)
    build_box.translate(0, branch_length, 0, pitch=first_branch_angle, yaw=0, roll=0)
    build_box.draw_line(0, 0, 0, 0, first_branch_length, 0,
                        r=color[0], g=color[1], b=color[2])
    build_box.send_data()
    sleep(0.5)
    draw_three_branches(count, first_branch_length)

    # second branch
    build_box.clear_data()
    build_box.change_shape('sphere')
    build_box.set_command('float')
    second_branch_length = branch_length * length_ratio * uniform(0.8, 1.2)
    second_branch_angle = angle_to_open * uniform(0.8, 1.2)
    build_box.translate(0, branch_length, 0, pitch=second_branch_angle, yaw=120, roll=0)
    build_box.draw_line(0, 0, 0, 0, second_branch_length, 0,
                        r=color[0], g=color[1], b=color[2])
    build_box.send_data()
    sleep(0.5)
    draw_three_branches(count, second_branch_length)

    # third branch
    build_box.clear_data()
    build_box.change_shape('sphere')
    build_box.set_command('float')
    third_branch_length = branch_length * length_ratio * uniform(0.8, 1.2)
    third_branch_angle = angle_to_open * uniform(0.8, 1.2)
    build_box.translate(0, branch_length, 0, pitch=third_branch_angle, yaw=240, roll=0)
    build_box.draw_line(0, 0, 0, 0, third_branch_length, 0,
                        r=color[0], g=color[1], b=color[2])
    build_box.send_data()
    sleep(0.5)
    draw_three_branches(count, third_branch_length)

    print('pop_matrix')
    build_box.pop_matrix()


room_name = "1000"
build_box = BuildBox(room_name)
initial_length = 10
repeat_count = 5
angle_to_open = 30
length_ratio = 0.75
trunk_color = (0.5, 0, 0)
leaf_color = (0, 0.5, 0)

build_box.change_shape('sphere')
build_box.set_command('float')
build_box.draw_line(0, 0, 0, 0, initial_length, 0,
                    r=trunk_color[0], g=trunk_color[1], b=trunk_color[2])
build_box.send_data()
sleep(0.5)

draw_three_branches(repeat_count, initial_length)
