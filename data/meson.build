desktop = custom_target(
    'desktop',
    input: 'org.bushidos.Techo.desktop.in.in',
    output: 'org.bushidos.Techo.desktop',
    command: [intltool_merge, '-d', '-u', po_dir, '@INPUT@', '@OUTPUT@'],
    install: true,
    install_dir: desktopdir,
)

appdata = custom_target(
    'appdata',
    input: 'org.bushidos.Techo.metainfo.xml.in',
    output: 'org.bushidos.Techo.metainfo.xml',
    command: [intltool_merge, '-x', '-u', po_dir, '@INPUT@', '@OUTPUT@'],
    install: true,
    install_dir: join_paths(datadir, 'metainfo'),
)

schema_conf = configuration_data()
schema_conf.set('GETTEXT_PACKAGE', 'techo')

schema_file = configure_file(
    input: 'org.bushidos.Techo.gschema.xml.in',
    output: 'org.bushidos.Techo.gschema.xml',
    configuration: schema_conf,
    install_dir: join_paths(datadir, 'glib-2.0', 'schemas')
)

service_conf = configuration_data()
service_conf.set('bindir', join_paths(prefix, bindir))

configure_file(
    input: 'org.bushidos.Techo.service.in',
    output: 'org.bushidos.Techo.service',
    configuration: service_conf,
    install_dir: join_paths(datadir, 'dbus-1', 'services')
)

install_data(
    'techo.1',
    install_dir : join_paths(get_option('prefix'), get_option('mandir'), 'man1')
)

install_data(
    'xed.xml',
    install_dir: join_paths(datadir, 'techo', 'styles')
)

install_data(
    'styles/bushidos-neon.xml',
    'styles/bushidos-classic.xml',
    install_dir: join_paths(datadir, 'techo', 'styles')
)

# App icon
foreach size : ['16x16', '22x22', '24x24', '32x32', '48x48', '64x64', '128x128', '256x256']
    install_data(
        join_paths('icons', 'hicolor', size, 'apps', 'org.bushidos.Techo.png'),
        install_dir: join_paths(datadir, 'icons', 'hicolor', size, 'apps')
    )
endforeach

install_data(
    join_paths('icons', 'hicolor', 'scalable', 'apps', 'org.bushidos.Techo.svg'),
    install_dir: join_paths(datadir, 'icons', 'hicolor', 'scalable', 'apps')
)
