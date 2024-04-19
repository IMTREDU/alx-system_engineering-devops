# Puppet manifest to install Flask version 2.1.0 using pip3
# Ensure the flask package is installed with version 2.1.0
package { 'flask':
  ensure   => '2.1.0',
  provider => pip3,
}
