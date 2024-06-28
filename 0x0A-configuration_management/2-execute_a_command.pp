# Using Puppet, create a manifest that kills a process named killmenow.
exec { 'kill_killmenow':
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
}
