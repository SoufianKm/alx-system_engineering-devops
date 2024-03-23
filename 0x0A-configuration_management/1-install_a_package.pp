#Install flask from pip3

package { 'flask':
  ensure   => 'latest',
  provider => 'pip3',
}

package { 'werkzeug':
  ensure   => 'latest',
  provider => 'pip3',
}

