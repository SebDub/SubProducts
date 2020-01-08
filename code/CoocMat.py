def GettingCoocurenceMatrix(dirName: str = 'data'):

    import pandas as pd
    import scipy.sparse as sparse

    dirName = 'data'

    PriorOrders = pd.read_csv(f'{dirName}/order_products__prior.csv')
    TrainOrders = pd.read_csv(f'{dirName}/order_products__train.csv')

    OrdersMerged = PriorOrders.append(TrainOrders)
    OrdersMerged.drop(['add_to_cart_order', 'reordered'],
                      axis=1, inplace=True)

    del PriorOrders
    del TrainOrders

    # Create mappings of the products and the orders
    # for the order we don't really care about the idx_to_order
    order_to_idx = {}
    idx_to_order = {}
    for (idx, oid) in enumerate(OrdersMerged.order_id.unique().tolist()):
        order_to_idx[oid] = idx
        idx_to_order[idx] = oid

    prod_to_idx = {}
    idx_to_prod = {}
    for (idx, prodid) in enumerate(OrdersMerged.product_id.unique().tolist()):
        prod_to_idx[prodid] = idx
        idx_to_prod[idx] = prodid

    OrdersMerged['prod_idx'] = OrdersMerged['product_id'].map(prod_to_idx)
    OrdersMerged['ord_idx'] = OrdersMerged['order_id'].map(order_to_idx)

    Occur = [1]*OrdersMerged.shape[0]
    OccurRow = OrdersMerged['ord_idx'].to_list()
    OccurCol = OrdersMerged['prod_idx'].to_list()

    SparseMat = sparse.csr_matrix((Occur, (OccurRow, OccurCol)),
                                  shape=(len(order_to_idx),
                                  len(idx_to_prod)))
    # Make Coocurence matrix
    Cooc_Mat = SparseMat.T.dot(SparseMat)
    Cooc_Mat.setdiag(0)

    print(Cooc_Mat[100, :].max())
    print(Cooc_Mat[100, :].argmax())
    print(idx_to_prod[100])
    print(idx_to_prod[Cooc_Mat[100, :].argmax()])
