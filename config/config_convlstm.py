import argparse


def parse_args():
    parser = argparse.ArgumentParser(
            description='convlstm model')
    """Tran, test"""
    parser.add_argument('--mode', required=True, help='choose running mode, 0 for train, 1 for test, 2 for both')
    """Model"""
    parser.add_argument('--kernal_size', required=4, help='kernal size, int or tuple')
    parser.add_argument('--input_dim', required=64, help='input dimension')
    parser.add_argument('--hidden_dim', required=16, help='input dimension')
    parser.add_argument('--num_layers', required=1, help='input dimension')
    parser.add_argument('--batch_first', default=True, help='convlstm model, batch first, change in convlstm.py')
    parser.add_argument('--return_all_layers', default=False, help='return all layers')
    parser.add_argument('--bias', default=True, help='bias')


    # parser.add_argument('--config', default="", help='config file for the model')
    # parser.add_argument('--checkpoint', default='./checkpoint/', help='checkpoint file path')
    # parser.add_argument('--load_ckpt', default='checkpoint/01_23_23_08_step6_in288/ckpts_best/epoch_133_trainloss0.0001', help='path to load ckpt')
    # parser.add_argument('--load', default=False, help='if load checkpoint or train a new model')
    # parser.add_argument('--save_improved_model', default=False, help='if save all improved models')
    # parser.add_argument('--input_size', default=1, help='lstm model input length')
    # parser.add_argument('--output_size', default=6, help='model prediction steps')
    # parser.add_argument('--hidden_size', default=64, help='lstm network cell numbers in each layer')
    # parser.add_argument('--learning_rate', default=0.0001, help='learning rate')
    # parser.add_argument('--weight_decay', default=0.01, help='weight decay')
    # parser.add_argument('--epoch', default=400, help='training epochs')
    # parser.add_argument('--batch_size', default=288, help='train window, 288 represent 288 steps -- 24hrs')
    # parser.add_argument('--seq_len', default=288, help='length of the sentence or time-series sequence used for pred')
    # parser.add_argument('--num_layers', default=3, help='number of lstm layers, assuming ')
    # parser.add_argument('--batch_first', default=True, help='lstm model, batch first, change in dac_lstm.py')
    """Dataset"""
    # parser.add_argument('--split', default=0.7, help='split train and test dataset, with train = split * dataset')
    # parser.add_argument('--cols', default=['0'], help='columns used in the dataset')
    # parser.add_argument('--normalisation', default=True, help='normalise dataset')
    """File Path"""
    # parser.add_argument('--file_path', default='./dataset/data_220.csv', help='file path')

    args = parser.parse_args()

    return args
