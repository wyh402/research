require "json"
require "csv"

hash_ary = []

 File.open("departments.json","w") do |json|
   CSV.foreach("departments.txt",col_sep: "\t", headers: true) do |line|
    h = {keyword: line[0], department: line[2]}
    hash_ary << h
  end
 Use JSON.dump (hash_ary, json) #to_json
end