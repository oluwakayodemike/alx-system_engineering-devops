#!/usr/bin/env ruby

regex = /School/
string = ARGV[0]

if string =~ regex
  puts string.match(regex)
else
  puts ""
end

