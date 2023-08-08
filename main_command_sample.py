from build_box import BuildBox

room_name = "1000"
build_box = BuildBox(room_name)

build_box.set_box_size(0.3)
build_box.set_build_interval(0.01)

# build_box.set_command('axis')
build_box.set_command('japaneseCastle')

build_box.send_data()
