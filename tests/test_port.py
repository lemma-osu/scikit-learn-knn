from numpy.testing import assert_array_almost_equal, assert_array_equal
from sklearn.model_selection import train_test_split

from sklearn_knn import GNN, Euclidean, Mahalanobis, Raw


def test_moscow_raw(moscow_raw):
    X_train, X_test, y_train, _ = train_test_split(
        moscow_raw.X, moscow_raw.ids, train_size=0.8, shuffle=False
    )
    clf = Raw(n_neighbors=5).fit(X_train, y_train)

    dist, _ = clf.kneighbors()
    nn = clf.kneighbor_ids()

    assert_array_equal(nn, moscow_raw.ref_neighbors)
    assert_array_almost_equal(dist, moscow_raw.ref_distances, decimal=3)

    dist, _ = clf.kneighbors(X_test)
    nn = clf.kneighbor_ids(X_test)

    assert_array_equal(nn, moscow_raw.trg_neighbors)
    assert_array_almost_equal(dist, moscow_raw.trg_distances, decimal=3)


def test_moscow_euclidean(moscow_euclidean):
    X_train, X_test, y_train, _ = train_test_split(
        moscow_euclidean.X, moscow_euclidean.ids, train_size=0.8, shuffle=False
    )
    clf = Euclidean(n_neighbors=5).fit(X_train, y_train)

    dist, _ = clf.kneighbors()
    nn = clf.kneighbor_ids()

    assert_array_equal(nn, moscow_euclidean.ref_neighbors)
    assert_array_almost_equal(dist, moscow_euclidean.ref_distances, decimal=3)

    dist, _ = clf.kneighbors(X_test)
    nn = clf.kneighbor_ids(X_test)

    assert_array_equal(nn, moscow_euclidean.trg_neighbors)
    assert_array_almost_equal(dist, moscow_euclidean.trg_distances, decimal=3)


def test_moscow_mahalanobis(moscow_mahalanobis):
    X_train, X_test, y_train, _ = train_test_split(
        moscow_mahalanobis.X, moscow_mahalanobis.ids, train_size=0.8, shuffle=False
    )
    clf = Mahalanobis(n_neighbors=5).fit(X_train, y_train)

    dist, _ = clf.kneighbors()
    nn = clf.kneighbor_ids()

    assert_array_equal(nn, moscow_mahalanobis.ref_neighbors)
    assert_array_almost_equal(dist, moscow_mahalanobis.ref_distances, decimal=3)

    dist, _ = clf.kneighbors(X_test)
    nn = clf.kneighbor_ids(X_test)

    assert_array_equal(nn, moscow_mahalanobis.trg_neighbors)
    assert_array_almost_equal(dist, moscow_mahalanobis.trg_distances, decimal=3)


def test_moscow_gnn(moscow_gnn):
    X_train, X_test, y_train, _, y_spp, _ = train_test_split(
        moscow_gnn.X, moscow_gnn.ids, moscow_gnn.y, train_size=0.8, shuffle=False
    )
    clf = GNN(n_neighbors=5).fit(X_train, y_train, spp=y_spp)

    dist, _ = clf.kneighbors()
    nn = clf.kneighbor_ids()

    assert_array_equal(nn, moscow_gnn.ref_neighbors)
    assert_array_almost_equal(dist, moscow_gnn.ref_distances, decimal=3)

    dist, _ = clf.kneighbors(X_test)
    nn = clf.kneighbor_ids(X_test)

    assert_array_equal(nn, moscow_gnn.trg_neighbors)
    assert_array_almost_equal(dist, moscow_gnn.trg_distances, decimal=3)
