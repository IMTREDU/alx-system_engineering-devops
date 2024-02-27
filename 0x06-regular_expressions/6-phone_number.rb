#!/usr/bin/env ruby

regex = /^\d{10}$/
input = ARGV[0]

if input
  puts input.match?(regex) ? input : ""
else
  puts "No input provided."
end
