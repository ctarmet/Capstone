import numpy as np

def original_polytope(n):
    # Important that the first 2 vertices constitute an edge that is parallel with 4th dim-axis
    # That is, a pair of coordinates that only differs in the 4th dim-value
    # Also, the first vertex should have a smaller 4D-value compared to the second vertex
    if n == 5: # Regular 5-cell
        a = np.sqrt(10)
        b = np.sqrt(6)
        c = np.sqrt(3)
        vertices = np.array([[1/a, 1/b, 1/c, -1], [1/a, 1/b, 1/c, 1], [1/a, 1/b, -2/c, 0], [1/a, -np.sqrt(3/2), 0, 0], [-2*np.sqrt(2/5), 0, 0, 0]])

        return vertices
    
    if n == 8: # Regular 16-cell
        vertices = np.array([[0,0,0,-1], [0,0,0,1], [-1,0,0,0], [1,0,0,0], [0,-1,0,0], [0,1,0,0], [0,0,-1,0], [0,0,1,0]])
        return vertices
    
    if n == 16: # Regular 8-cell (hypercube)
        vertices = np.array([[-1,-1,-1,-1], [-1,-1,-1,1], [-1,-1,1,-1], [-1,-1,1,1], [-1,1,-1,-1], [-1,1,-1,1], [-1,1,1,-1], [-1,1,1,1], [1,-1,-1,-1], [1,-1,-1,1], [1,-1,1,-1], [1,-1,1,1], [1,1,-1,-1], [1,1,-1,1], [1,1,1,-1], [1,1,1,1]])
        return vertices    
    
    if n == 24: # Regular 24-cell
        a = 0.5
        b = -0.5
        vertices = np.array([[b,b,b,b], [b,b,b,a], [b,b,a,b], [b,b,a,a], [b,a,b,b], [b,a,b,a], [b,a,a,b], [b,a,a,a], [a,b,b,b], [a,b,b,a], [a,b,a,b], [a,b,a,a], [a,a,b,b], [a,a,b,a], [a,a,a,b], [a,a,a,a], [-1,0,0,0], [1,0,0,0], [0,-1,0,0], [0,1,0,0], [0,0,-1,0], [0,0,-1,0], [0,0,0,-1], [0,0,0,1]])
        return vertices
    
    # The other 2 has 120 and 600 vertices respectively
    

def affine(vertices, r, n):
    # Determine the coordinates of the scaled vertices after each affine transformation
    scaled_vertices = []
    for i in range(n):
        fixed_vertex = vertices[i]
        transformation = (1-r)*vertices + r*fixed_vertex
        scaled_vertices.append(transformation)

    # Returns |V| sets of scaled coordinates. One set of |V| coordinates for each v_i in V
    return scaled_vertices


def overlap_test(n, r):
    """Iteratively increase r until there is no overlap.
    If the x-coordinates are not close enough, iteratively decrese r until 
    they are closer than the accepted error"""
    # Generate the original vertices
    vertices = original_polytope(n)
    original_side_length = get_side_length(vertices)
    print(f"Original side length: {original_side_length}")

    # iterate over r starting at an initial point and going towards 1
    while r < 1:
        print(f"\nChecking for r = {r}")

        # Find the scaled vertices for this r
        scaled_vertices = affine(vertices, r, n)

        # Only needed to check the 4D-coords of two regions because of the symmetry
        # We use the indicies 0 and 1 since they are 2 vertices that gives an edge parallel to the 4D-axis
        # See original_polytope comments for better understanding
        region1 = scaled_vertices[0]
        region2 = scaled_vertices[1]

        # Initialize the list of 4D-values for the 2 regions
        region1_4D = []
        region2_4D = []

        # Find the 4D-values of the transformed vertices
        for i in range(len(region1)):
            coord = region1[i]
            region1_4D.append(coord[3])
        
        for i in range(len(region2)):
            coord = region2[i]
            region2_4D.append(coord[3])

        r1max = max(region1_4D) # The largest 4D-value of the first region
        r2min = min(region2_4D) # The smallest 4D-value of the second region

        # Calculate dm in conjectured ropt formula. Note that these are the original polytopes vertex-coordinates
        dim_4s = []
        for i in range(n):
            vertex = vertices[i]
            dim_4s.append(vertex[3])
            
        # Since all polytopes are oriented with the edge between vertices[0] and vertices[1] being parallel with the x-axis
        dm = max(dim_4s) - min(dim_4s)

        
        # Check if overlap occurs
        if r1max - r2min > 0.000001:
            print(f"Overlap detected at r = {r}")

            # Increase r and continue
            r += 0.00001

        elif abs(r1max - r2min) < 0.000001: # Accepted error. Will give at least 5 correct decimals
            print(f"Experimental Optimal Ratio Achieved\nr = {r}")
            # Print conjectured optimal ratio, dm, and edge length
            print(f"Conjectured Optimal Ratio: {dm/(dm + original_side_length)}") 
            print(f"dm = {dm}")
            edgelength = get_side_length(vertices)
            print(f"Edge length = {edgelength}")
            print(f"dm in terms of edge length: {dm/edgelength} * edgelength")

            return r

        else:
            # Regions are no longer touching
            print(f"Regions not touching for r = {r}")

            r -= 0.0000001
            

def get_side_length(vertices):
    # Compute the side length of a polygon determined by it's vertices
     return np.linalg.norm(vertices[0] - vertices[1])


overlap_test(24, 0.48)