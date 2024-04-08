def convertir_a_Tree(dendo, leaf_names):
      from scipy.cluster import hierarchy
      """
      Convierte la salida de scipy.cluster.hierarchy.to_tree a un objeto ete3.Tree.
      """
      tree1 = hierarchy.to_tree(dendo, False)
      newick_tree1 = get_newick(tree1, tree1.dist, leaf_names)
      tree = ete3.Tree(newick_tree1)

      return tree
