# Using Puppet, install flask from pip3 
# Install an especific version Werkzeug (2.1.1)

package { ['flask', 'werkzeug']:
  ensure   => '2.1.0',
  provider => 'pip3'
}

exec { 'install_werkzeug':
  command     => '/usr/bin/pip3 install Werkzeug==2.1.1',
  path        => ['/usr/bin', '/usr/local/bin'],
  environment => ['PATH=/usr/bin:/usr/local/bin'],
  unless      => '/usr/bin/pip3 show Werkzeug | grep -q "Version: 2.1.1"',
  require     => Package['python3-pip'],
}

