# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define the custom HTTP header configuration
file { '/etc/nginx/conf.d/custom_headers.conf':
  ensure  => present,
  content => "add_header X-Served-By $hostname;\n",
  notify  => Service['nginx'],
}

# Manage Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
