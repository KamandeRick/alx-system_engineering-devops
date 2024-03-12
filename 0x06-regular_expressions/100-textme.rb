#!/usr/bin/env ruby

if ARGV.length == 1
  SENDER,RECEIVER,FLAGS  = ARGV[0].match(/^.*\[from:(.*?)\].*\[to:(.*?)\].*\[flags:(.*?)\].*$/i).captures
  puts "#{SENDER}#{RECEIVER}#{FLAGS}"
  exit
end
