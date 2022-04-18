#Desc

file_line {'ssh_config':
ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => "PasswordAuthentication no",
  match  => 'PasswordAuthentication yes',
}
file_line {'ssh config':
ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => "IdentityFile ~/.ssh/school",
  match  => 'IdentityFile ~/.ssh/school',
}