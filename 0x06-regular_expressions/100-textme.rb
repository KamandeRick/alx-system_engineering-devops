#!/usr/bin/env ruby

if ARGV.length == 1
  sender = ARGV[0].match(/^.*\[from:(.*?)\]/).captures
  exit
end
