# Using Puppet to install flask using pip3
package { 'python3-pip':
  ensure => present,
}

exec { 'install-flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => ['/usr/bin', '/bin'],
  creates => '/usr/local/bin/flask',
}


