# Define an exec resource to kill the process named killmenow using pkill
exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => '/bin:/usr/bin:/sbin:/usr/sbin',
  logoutput   => true,
  refreshonly => true,
}
