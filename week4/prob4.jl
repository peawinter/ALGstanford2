# Read data
fin = "/Users/shunyong/ACE/Coursera/Algorithm Stanford 2/week4/" * "g3.txt"
f = open(fin, "r")
raw = split(readline(f), ' ')
nV = int(raw[1])
nE = int(raw[2])

rawData = readdlm(fin, ' ', skipstart = 1, Int)
gdict = [(rawData[i, 1], rawData[i, 2]) => rawData[i, 3] for i = 1:nE]

# # detect negative cycly
# curr_dist = ones(Int, nV) * Inf16
# curr_dist[1] = 0
# predecessor = zeros(Int, nV)
# new_dist = copy(curr_dist)
# for i = 1:nV
#   for edge in keys(gdict)
#     (u, v) = edge
#     if curr_dist[u] + gdict[edge] < new_dist[v]
#       new_dist[v] = curr_dist[u] + gdict[edge]
#       predecessor[v] = u
#     end
#   end
#   curr_dist = copy(new_dist)
# end

# for edge in keys(gdict)
#   (u, v) = edge
#   if curr_dist[u] + gdict[edge] < curr_dist[v]
#     println("Error, graph g3 contains a negative weight cycle")
#     break
#   end
# end

# println(curr_dist)

curr_mat = ones(Int, nV, nV) * Inf16
for idxRow = 1 : nE
  curr_mat[rawData[idxRow, 1], rawData[idxRow, 2]] = rawData[idxRow, 3]
end
for idx = 1 : nV
  curr_mat[idx, idx] = 0
end
next_mat = copy(curr_mat)
for k = 1:nV
  for i = 1:nV
    for j = 1:nV
      next_mat[i, j]=min(next_mat[i, j], curr_mat[i, k] + curr_mat[k, j])
    end
  end
  curr_mat = copy(next_mat)
end
println(minimum(curr_mat))