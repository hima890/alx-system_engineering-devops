exec { 'kill_killmenow':
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
}
