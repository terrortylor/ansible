%w[lazygit tmux fzf bat nmap lastpass-cli].each do |package|
  describe package(package) do
    it { should be_installed }
  end
end

%w[rg fd].each do |binary|
  describe file("/usr/bin/#{binary}") do
    it { should exist }
  end
end

%w[gron].each do |binary|
  describe file("/usr/local/bin/#{binary}") do
    it { should exist }
  end
end

describe file('/etc/yum.repos.d/_copr:copr.fedorainfracloud.org:atim:lazygit.repo') do
  it { should exist }
end
