from numpy.testing import assert_array_almost_equal
from sklearn.model_selection import train_test_split

from sknnr import (
    EuclideanKNNRegressor,
    GNNRegressor,
    MahalanobisKNNRegressor,
    MSNRegressor,
    RawKNNRegressor,
)


def yaimpute_weights(d):
    return 1.0 / (1.0 + d)


def test_moscow_raw(moscow_raw):
    X_train, X_test, y_train, _ = train_test_split(
        moscow_raw.X, moscow_raw.y, train_size=0.8, shuffle=False
    )
    clf = RawKNNRegressor(n_neighbors=5).fit(X_train, y_train)

    dist, nn = clf.kneighbors()

    # assert_array_equal(nn, moscow_raw.ref_neighbors)
    assert_array_almost_equal(dist, moscow_raw.ref_distances, decimal=3)

    dist, nn = clf.kneighbors(X_test)

    # assert_array_equal(nn, moscow_raw.trg_neighbors)
    assert_array_almost_equal(dist, moscow_raw.trg_distances, decimal=3)

    prd = clf.predict(X_test)
    assert_array_almost_equal(prd, moscow_raw.trg_predicted_unweighted, decimal=3)

    clf = RawKNNRegressor(n_neighbors=5, weights=yaimpute_weights).fit(X_train, y_train)
    prd = clf.predict(X_test)
    assert_array_almost_equal(prd, moscow_raw.trg_predicted_weighted, decimal=3)


def test_moscow_euclidean(moscow_euclidean):
    X_train, X_test, y_train, _ = train_test_split(
        moscow_euclidean.X, moscow_euclidean.y, train_size=0.8, shuffle=False
    )
    clf = EuclideanKNNRegressor(n_neighbors=5).fit(X_train, y_train)

    dist, nn = clf.kneighbors()

    # assert_array_equal(nn, moscow_euclidean.ref_neighbors)
    assert_array_almost_equal(dist, moscow_euclidean.ref_distances, decimal=3)

    dist, nn = clf.kneighbors(X_test)

    # assert_array_equal(nn, moscow_euclidean.trg_neighbors)
    assert_array_almost_equal(dist, moscow_euclidean.trg_distances, decimal=3)

    prd = clf.predict(X_test)
    assert_array_almost_equal(prd, moscow_euclidean.trg_predicted_unweighted, decimal=3)

    clf = EuclideanKNNRegressor(n_neighbors=5, weights=yaimpute_weights).fit(
        X_train, y_train
    )
    prd = clf.predict(X_test)
    assert_array_almost_equal(prd, moscow_euclidean.trg_predicted_weighted, decimal=3)


def test_moscow_mahalanobis(moscow_mahalanobis):
    X_train, X_test, y_train, _ = train_test_split(
        moscow_mahalanobis.X, moscow_mahalanobis.y, train_size=0.8, shuffle=False
    )
    clf = MahalanobisKNNRegressor(n_neighbors=5).fit(X_train, y_train)

    dist, nn = clf.kneighbors()

    # assert_array_equal(nn, moscow_mahalanobis.ref_neighbors)
    assert_array_almost_equal(dist, moscow_mahalanobis.ref_distances, decimal=3)

    dist, nn = clf.kneighbors(X_test)

    # assert_array_equal(nn, moscow_mahalanobis.trg_neighbors)
    assert_array_almost_equal(dist, moscow_mahalanobis.trg_distances, decimal=3)

    prd = clf.predict(X_test)
    assert_array_almost_equal(
        prd, moscow_mahalanobis.trg_predicted_unweighted, decimal=3
    )

    clf = MahalanobisKNNRegressor(n_neighbors=5, weights=yaimpute_weights).fit(
        X_train, y_train
    )
    prd = clf.predict(X_test)
    assert_array_almost_equal(prd, moscow_mahalanobis.trg_predicted_weighted, decimal=3)


def test_moscow_msn(moscow_msn):
    X_train, X_test, y_train, _ = train_test_split(
        moscow_msn.X, moscow_msn.y, train_size=0.8, shuffle=False
    )
    clf = MSNRegressor(n_neighbors=5).fit(X_train, y_train, spp=y_train)

    dist, nn = clf.kneighbors()

    # assert_array_equal(nn, moscow_msn.ref_neighbors)
    assert_array_almost_equal(dist, moscow_msn.ref_distances, decimal=3)

    dist, nn = clf.kneighbors(X_test)

    # assert_array_equal(nn, moscow_msn.trg_neighbors)
    assert_array_almost_equal(dist, moscow_msn.trg_distances, decimal=3)

    prd = clf.predict(X_test)
    assert_array_almost_equal(prd, moscow_msn.trg_predicted_unweighted, decimal=3)

    clf = MSNRegressor(n_neighbors=5, weights=yaimpute_weights).fit(X_train, y_train)
    prd = clf.predict(X_test)
    assert_array_almost_equal(prd, moscow_msn.trg_predicted_weighted, decimal=3)


def test_moscow_gnn(moscow_gnn):
    X_train, X_test, y_train, _ = train_test_split(
        moscow_gnn.X, moscow_gnn.y, train_size=0.8, shuffle=False
    )
    clf = GNNRegressor(n_neighbors=5).fit(X_train, y_train, spp=y_train)

    dist, nn = clf.kneighbors()

    # assert_array_equal(nn, moscow_gnn.ref_neighbors)
    assert_array_almost_equal(dist, moscow_gnn.ref_distances, decimal=3)

    dist, nn = clf.kneighbors(X_test)

    # assert_array_equal(nn, moscow_gnn.trg_neighbors)
    assert_array_almost_equal(dist, moscow_gnn.trg_distances, decimal=3)

    prd = clf.predict(X_test)
    assert_array_almost_equal(prd, moscow_gnn.trg_predicted_unweighted, decimal=3)

    clf = GNNRegressor(n_neighbors=5, weights=yaimpute_weights).fit(X_train, y_train)
    prd = clf.predict(X_test)
    assert_array_almost_equal(prd, moscow_gnn.trg_predicted_weighted, decimal=3)
