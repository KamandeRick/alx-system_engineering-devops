#!/usr/bin/env ruby

if ARGV.length == 1
  puts ARGV[0].scan(/h\wn/).join
  exit
end
