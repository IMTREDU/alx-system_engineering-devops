#!/usr/bin/env ruby

input = ARGV[0]

if input
  puts input.scan(/hbt{2,5}n/).join
else
  puts "No input provided."
end
