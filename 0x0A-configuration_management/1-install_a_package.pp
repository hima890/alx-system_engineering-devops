class { 'python':
  version    => '3',
  pip        => 'present',
  dev        => 'present',
  virtualenv => 'present',
}

python::pip { 'flask':
  ensure  => '2.1.0',
  virtualenv => '/usr/local/bin/virtualenv',
  pip_provider => 'pip3',
  require => Class['python'],
}
