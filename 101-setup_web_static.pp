# Ensure the required packages are installed
package { 'nginx':
  ensure => installed,
}

# Ensure the directory structure is created
file { '/data/web_static/releases/test':
  ensure => directory,
  owner  => 'root',
  group  => 'root',
  mode   => '0755',
  require => Package['nginx'],
}

file { '/data/web_static/shared':
  ensure => directory,
  owner  => 'root',
  group  => 'root',
  mode   => '0755',
}

file { '/data/web_static/releases':
  ensure => directory,
  owner  => 'root',
  group  => 'root',
  mode   => '0755',
}

file { '/data/web_static':
  ensure => directory,
  owner  => 'root',
  group  => 'root',
  mode   => '0755',
}

# Ensure the HTML file is created
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

# Ensure the symbolic link is created
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
  owner  => 'root',
  group  => 'root',
  mode   => '0755',
  require => File['/data/web_static/releases/test'],
}

# Ensure Nginx is configured to serve the content
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Ensure the Nginx service is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

# Template for Nginx configuration
file { '/etc/nginx/sites-available/hbnb_static':
  ensure  => file,
  content => template('nginx/hbnb_static.erb'),
  notify  => Service['nginx'],
}

file { '/etc/nginx/sites-enabled/hbnb_static':
  ensure => link,
  target => '/etc/nginx/sites-available/hbnb_static',
  require => File['/etc/nginx/sites-available/hbnb_static'],
}
