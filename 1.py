edim = 100
# kdim = 100
vdim =200
kdim = kdim if kdim is not None else edim
# qkv_same_dim = kdim == embed_dim and vdim == embed_dim
print('kime')
print('kdim=',kdim)
# print('qkv_dim=',qkv_same_dim)
 """
    Transformer encoder consisting of *args.encoder_layers* layers. Each layer
    is a :class:`TransformerEncoderLayer`.

    Args:
        args (argparse.Namespace): parsed command-line arguments
        dictionary (~fairseq.data.Dictionary): encoding dictionary
        embed_tokens (torch.nn.Embedding): input embedding
    """