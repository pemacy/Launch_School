# frozen_string_literal: true

# Sometimes, the documentation is going to leave you scratching your head.

# In a very early assignment at Launch School, you are tasked with writing a
# program that loads some text messages from a YAML file. We do this with YAML::load_file:

require 'yaml'
MESSAGES = YAML.load_file('ex9.yml')
# yaml is an alias for psych - the native yaml parser

# Find the documentation for YAML::load_file.
require 'psych'

MESSAGE = Psych.load_file('ex9.yml')
p MESSAGE
p MESSAGES
