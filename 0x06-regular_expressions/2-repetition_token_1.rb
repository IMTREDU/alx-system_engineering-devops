#!/usr/bin/env ruby

input = ARGV[0]

if input
  puts input.scan(/hb?t?n/).join
else
  puts "No input provided."
end
