# Using Puppet, install flask from pip3 
# Install an especific version Werkzeug (2.1.1)

package { 'Werkzeug':
  ensure => '2.1.1',
  provider => 'pip3',
}
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}