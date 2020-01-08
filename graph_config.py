#!/usr/bin/env python3
BASE_PATH = "./data/g13"


def get_torchbiggraph_config():

    config = dict(
        # I/O data
        entity_path=BASE_PATH,
        edge_paths=[f'{BASE_PATH}/graph-partitioned'],
        checkpoint_path=f'{BASE_PATH}/model',

        # Graph structure
        entities={
            'all': {'num_partitions': 1},
        },
        relations=[{
            'name': 'all_edges',
            'lhs': 'all',
            'rhs': 'all',
            'operator': 'complex_diagonal',
        }],
        dynamic_relations=False,

        # Scoring model
        dimension=100,
        global_emb=False,
        comparator='dot',

        # Training
        num_epochs=20,
        num_uniform_negs=100,
        loss_fn='softmax',
        lr=0.1,

        # Evaluation during training
        eval_fraction=0,  # to reproduce results, we need to use all training data
    )

    return config
