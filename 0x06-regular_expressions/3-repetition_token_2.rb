#!/usr/bin/env ruby

input = ARGV[0]

if input
  puts input.scan(/hbt+n/).join
else
  puts "No input provided."
end
