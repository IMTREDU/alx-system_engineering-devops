# This Puppet manifest ensures the PHP configuration file is present and restarts Apache

file { '/etc/php5/apache2/php.ini':
  ensure  => file,
  source  => 'puppet:///modules/custom/php.ini',
  mode    => '0644',
  require => Package['php5'],
}

service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/php5/apache2/php.ini'],
}

exec { 'fix-permissions':
  command => 'chown www-data:www-data /var/www/html -R && chmod 755 /var/www/html -R',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'test $(find /var/www/html -not -user www-data) -o $(find /var/www/html -not -group www-data)',
  require => Service['apache2'],
}

package { 'php5':
  ensure => installed,
}

# Ensure Apache is running
service { 'apache2':
  ensure => running,
  enable => true,
  require => Package['apache2'],
}

package { 'apache2':
  ensure => installed,
}
