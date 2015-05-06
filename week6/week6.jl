function prob4()
  rst = [0 for i = 1:6]

  for idx = 1:6
    fin = "/Users/shunyong/ACE/Coursera/Algorithm Stanford 2/week6/2sat" * string(idx) *".txt"
    f = open(fin, "r")
    raw = split(readline(f), ' ')
    count = int(raw[1])

    rules = readdlm(fin, ' ', skipstart = 1, Int)

    function genGraph(rules, count)
      graph = Dict()
      graph = [ i => Set() for i = -count:count]

      for i = 1:count
        node1 = rules[i, 1]
        node2 = rules[i, 2]
        push!(graph[-node1], node2)
        push!(graph[-node2], node1)
      end
      graph
    end

    graph = genGraph(rules, count)

    # strong connect component

    function checkConnect(graph, count)

      for i = 1:count
        posi_neighbor = Set([i])
        posi_visited = Set()

        while length(posi_neighbor) > 0
          node = pop!(posi_neighbor)
          push!(posi_visited, node)
          posi_neighbor = union(posi_neighbor, graph[node])
          posi_neighbor = setdiff(posi_neighbor, posi_visited)
        end

        nega_neighbor = Set([-i])
        nega_visited = Set()

        while length(nega_neighbor) > 0
          node = pop!(nega_neighbor)
          push!(nega_visited, node)
          nega_neighbor = union(nega_neighbor, graph[node])
          nega_neighbor = setdiff(nega_neighbor, nega_visited)
        end

        if in(-i, posi_visited) && in(i, nega_visited)
          println(-i, i)
          println("result: unsatisfiable")
          return 0
        end
      end
      println("result: satisfiable")
      return 1
    end

    rst[idx] = checkConnect(graph, count)
  end
  return rst
end

rst = prob4()

println(rst)