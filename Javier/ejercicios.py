urdf_tutorial_path = get_package_share_path('x3_reto_alejandro')





data_files=[
    ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
    (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
    (os.path.join('share', package_name, 'launch'), glob('launch/*')),
    (os.path.join('share', package_name, 'meshes'), glob('meshes/*.STL')),
    (os.path.join('share', package_name, 'meshes', 'Ackermann'), glob('meshes/Ackermann/ *. STL'))
    (os.path.join('share', package_name, 'meshes', 'mecanum'), glob('meshes/mecanum/ *. STL')),
    (os.path.join('share', package_name, 'meshes', 'sensor'), glob('meshes/sensor/ *. STL'))
]