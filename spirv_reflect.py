import jmake

jmake.setupenv()

workspace = jmake.Workspace('spirv_reflect')
project = jmake.Project('spirv_reflect', jmake.Target.STATIC_LIBRARY)
project.add(jmake.fullpath('spirv_reflect.cpp'))
project.include(jmake.fullpath('.'))
project.export(includes=jmake.fullpath('.'))

debug = project.filter('debug')
debug['debug'] = True

cli = jmake.Project('cli', jmake.Target.EXECUTABLE)
cli.add(jmake.fullpath('main.cpp'))
cli.add(jmake.fullpath('examples/arg_parser.cpp'))
cli.add(jmake.fullpath('common/output_stream.cpp'))
cli.depend(project)

debug = cli.filter('debug')
debug['debug'] = True

workspace.add(project)
workspace.add(cli)

jmake.generate(workspace)
