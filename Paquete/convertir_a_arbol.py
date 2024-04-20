def get_newick(node, parent_dist, leaf_names, newick='') -> str:
    """
    Convert sciply.cluster.hierarchy.to_tree()-output to Newick format.

    :param node: output of sciply.cluster.hierarchy.to_tree()
    :param parent_dist: output of sciply.cluster.hierarchy.to_tree().dist
    :param leaf_names: list of leaf names
    :param newick: leave empty, this variable is used in recursion.
    :returns: tree in Newick format
    """
    if node.is_leaf():
        return "%s:%.2f%s" % (leaf_names[node.id], parent_dist - node.dist, newick)
    else:
        if len(newick) > 0:
            newick = "):%.2f%s" % (parent_dist - node.dist, newick)
        else:
            newick = ");"
        newick = get_newick(node.get_left(), node.dist, leaf_names, newick=newick)
        newick = get_newick(node.get_right(), node.dist, leaf_names, newick=",%s" % (newick))
        newick = "(%s" % (newick)
        return newick
    
def convertir_a_Tree(dendo, leaf_names):
      import ete3
      from ete3 import Tree
      from scipy.cluster import hierarchy
      """
      Convierte la salida de scipy.cluster.hierarchy.to_tree a un objeto ete3.Tree.
      """
      tree1 = hierarchy.to_tree(dendo, False)
      from Paquete.get_netwick import get_newick
      newick_tree1 = get_newick(tree1, tree1.dist, leaf_names)
      tree = ete3.Tree(newick_tree1)

      return tree
