#!/usr/bin/env ruby
#A regular expression matching School

regex = /School/
string = ARGV[0]

if string =~ regex
  puts string.match(regex)
else
  puts ""
end

