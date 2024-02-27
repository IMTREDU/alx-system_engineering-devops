#!/usr/bin/env ruby

regex = /^h.n$/
input = ARGV[0]

if input
  puts input.match?(regex) ? input : ""
else
  puts "No input provided."
end
