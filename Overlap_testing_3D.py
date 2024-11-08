import numpy as np

def original_polytope(n):
    # Important that the first 2 vertices constitute an edge that is parallel with x-axis
    # That is, a pair of coordinates that only differs in the x-value.
    # Also, the first vertex should have a smaller x-value compared to the second vertex
    if n == 4:
        # Finding the vertices of a tetrahedron
        vertices = np.array([[-1,0,-1/(2**0.5)],[1,0,-1/(2**0.5)], [0,1,1/(2**0.5)],[0,-1,1/(2**0.5)]])
    
    if n == 6:
        # Finding the vertices of an octahedron
        vertices = np.array([[0,0,0], [1,0,0], [0,1,0], [1,1,0],[0.5,0.5,1/(2**0.5)],[0.5,0.5,-1/(2**0.5)]]) 

    if n == 8:
        # Finding the vertices of a cube
        vertices = np.array([[0,0,0], [1,0,0], [0,1,0], [0,0,1], [1,1,0], [1,0,1], [0,1,1], [1,1,1]])

    if n == 12:
        # Finding the vertices of an icosahedron
        phi = (1+np.sqrt(5))/2
        a = 1
        b = phi
        vertices = np.array([[-a, -b, 0], [a, -b, 0], [-a, b, 0], [a, b, 0], [0, -a, -b], [0, a, -b], [0, -a, b], [0, a, b], [-b, 0, -a], [-b, 0, a], [b, 0, -a], [b, 0, a] ])

    if n == 20:
        # Finding the vertices of a dodecahedron
        phi = (1+np.sqrt(5))/2
        a = 1
        b = phi
        c = a+b

        vertices = np.array([[-a, 0, -c], [a, 0, -c], [-b,-b,-b], [b,-b,-b], [-b,b,-b], [b,b,-b], [-b,-b,b], [b,-b,b], [-b,b,b], [b,b,b], [c, -a, 0], [c, a, 0], [-c, -a, 0], [-c, a, 0], [a, 0, c], [-a, 0, c], [0, -c, -a], [0, -c, a], [0, c, -a], [0, c, a]])
    return vertices
    
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

        # Only needed to check the x-coords of two regions because of the symmetry
        # We use the indicies 0 and 1 since they are 2 vertices that gives an edge parallel to the x-axis
        # See original_polytope comments for better understanding
        region1 = scaled_vertices[0]
        region2 = scaled_vertices[1]

        # Initialize the list of x-values for the 2 regions
        region1x = []
        region2x = []

        # Find the x-values of the transformed vertices
        for i in range(len(region1)):
            coord = region1[i]
            region1x.append(coord[0])
        
        for i in range(len(region2)):
            coord = region2[i]
            region2x.append(coord[0])

        r1xmax = max(region1x) # The largest x-value of the first region
        r2xmin = min(region2x) # The smallest x-value of the second region

        # Calculate dm in conjectured ropt formula. Note that these are the original polytopes vertex-coordinates
        xs = []
        for i in range(n):
            vertex = vertices[i]
            xs.append(vertex[0])
            
        # Since all polyhedra are oriented with the edge between vertices[0] and vertices[1] being parallel with the x-axis
        dm = max(xs) - min(xs)

        
        # Check if overlap occurs
        if r1xmax - r2xmin > 0.000001:
            print(f"Overlap detected at r = {r}")

            # Increase r and continue
            r += 0.00001

        elif abs(r1xmax - r2xmin) < 0.000001: # Accepted error. Will give at least 5 correct decimals
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

overlap_test(20, 0.7)