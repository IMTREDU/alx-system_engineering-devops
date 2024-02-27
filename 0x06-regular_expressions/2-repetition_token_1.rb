#!/usr/bin/env ruby

regex = /hbt+n/
input = ARGV[0]

if input
  puts input.scan(regex).join
else
  puts "No input provided."
end
