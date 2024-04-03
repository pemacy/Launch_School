def cleanup(str)
  str.gsub(/[^a-z]/i, ' ').squeeze
end

p cleanup("---what's my +* line?")
